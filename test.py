import argparse

def openfile():
    parser = argparse.ArgumentParser(description="CSVファイル名を受け取るサンプル")
    parser.add_argument("filename", help="読み込むCSVファイル名")
    args = parser.parse_args()
    return args

args = openfile()
print(f"指定されたファイル名: {args.filename}")