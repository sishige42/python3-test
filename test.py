import argparse
import os
import csv

# コマンドライン引数を受け取る関数
def get_input_filepaths():
    parser = argparse.ArgumentParser(description="CSVファイルの行列変換プログラム")
    parser.add_argument("input_filepaths", nargs="+", help="変換元のCSVファイルパス")
    args = parser.parse_args()
    return args

# CSVファイルを開く関数
def validate_and_open_input_csv(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Error: not found '{filepath}'")
    if not os.path.isfile(filepath):
        raise ValueError(f"Error: not file {filepath}")

    try:
        # 読み取りでファイルを開いて、csvリーダーを返す
        return open(filepath, 'r', newline='', encoding='utf-8')
    except Exception as e:
        raise IOError(f"Error: 読み込み失敗 {filepath}")

# 行列変換する関数
def transpose_csv_data(input_csv_reader):
    data = list(input_csv_reader)

    # データがからの処理
    if not data:
        return []

    # 行列変換
    transposed_data = list(map(list, zip(*data)))
    return transposed_data

# 出力先ファイルを作成する関数
def create_and_open_output_csv(output_filepath):
    try:
        # 書き込みでファイルを開いて、CSVライターを返す
        # 出力先がない場合は新規作成
        return open(output_filepath, 'a', newline='', encoding='utf-8')
    except Excepton as e:
        raise IOError(f"Error: 出力先エラー {output_filepath}")

def main():
    input_file_path = None
    input_csv_file = None
    output_csv_file = None

    try:
        # 1. コマンドライン引数から変換前ファイルパスを受け取る
        args = get_input_filepaths()

        for input_file_path in args.input_filepaths:

            # 2. コマンドライン引数のファイルパスチェック
            # withでファイルを勝手に閉じる
            with validate_and_open_input_csv(input_file_path) as input_csv_file:
                input_csv_reader = csv.reader(input_csv_file)

                # 3. 行列変換する(列を行にする)
                # 実際の変換ロジック関数を実装する
                transposed_data = transpose_csv_data(input_csv_reader)
    
                # 4. 出力先を分岐する関数を追加

                # 5. 出力先CSVのパスを決定、存在しなければ作成、出力先CSVを開く
                with create_and_open_output_csv("/Users/wota/github/python3-test/transposed.csv") as output_csv_file:
                    output_csv_writer = csv.writer(output_csv_file)
                    output_csv_writer.writerows(transposed_data)
            

    except FileNotFoundError as e:
        print(f"1: {e}")
    except ValueError as e:
        print(f"2: {e}")
    except IOError as e:
        print(f"3: {e}")
    except Exception as e:
        print(f"予期せぬエラー: {e}")
    finally:
        
        pass

if __name__ == "__main__":
    main()
