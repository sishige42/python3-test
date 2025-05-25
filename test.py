import argparse

def openfile():
    parser = argparse.ArgumentParser(description="CSVファイル名を受け取るサンプル")
    parser.add_argument("files", nargs="+", help="読み込むCSVファイル名")
    args = parser.parse_args()
    return args

args = openfile()
for filename in args.files:
    print(f"指定されたファイル名: {filename}")