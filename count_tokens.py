import os
import tiktoken
import matplotlib.pyplot as plt
import numpy as np

def get_md_files(root_dir):
    md_files = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(subdir, file))
    return md_files

def count_tokens_in_file(file_path, encoding):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return len(encoding.encode(text))

def main():
    root_dir = './docs'
    md_files = get_md_files(root_dir)
    encoding = tiktoken.get_encoding("cl100k_base")

    token_counts = []
    for file in md_files:
        tokens = count_tokens_in_file(file, encoding)
        token_counts.append(tokens)
        print(f"{file}: {tokens} tokens")

    if token_counts:
        avg_tokens = np.mean(token_counts)
        median_tokens = np.median(token_counts)
        min_tokens = np.min(token_counts)
        max_tokens = np.max(token_counts)
        std_tokens = np.std(token_counts)
        p90_tokens = np.percentile(token_counts, 90)

        print(f"\nTotal files: {len(token_counts)}")
        print(f"Average tokens: {avg_tokens:.2f}")
        print(f"Median tokens: {median_tokens}")
        print(f"Min tokens: {min_tokens}")
        print(f"Max tokens: {max_tokens}")
        print(f"Standard deviation: {std_tokens:.2f}")
        print(f"90th percentile: {p90_tokens:.0f}")

        bins = [0, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
        hist, bin_edges = np.histogram(token_counts, bins=bins)
        print("\nFile count by token range:")
        for i in range(len(hist)):
            print(f"{int(bin_edges[i])}-{int(bin_edges[i+1])}: {hist[i]} files")

        plt.figure(figsize=(12,7))
        plt.hist(token_counts, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
        plt.title('Distribution of Token Counts in Markdown Files')
        plt.xlabel('Number of Tokens')
        plt.ylabel('Number of Files')
        plt.grid(axis='y', alpha=0.75)

        plt.axvline(avg_tokens, color='red', linestyle='dashed', linewidth=1.5, label=f'Mean: {avg_tokens:.0f}')
        plt.axvline(median_tokens, color='green', linestyle='dashed', linewidth=1.5, label=f'Median: {median_tokens:.0f}')
        plt.axvline(p90_tokens, color='purple', linestyle='dashed', linewidth=1.5, label=f'90th %ile: {p90_tokens:.0f}')
        plt.legend()

        plt.tight_layout()
        plt.show()
    else:
        print("No markdown files found.")

if __name__ == "__main__":
    main() 