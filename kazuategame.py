# 数当てゲーム
# 1〜100の間の整数をランダムに選択し、ユーザーが当てるゲーム

import random

def main():
    """数当てゲームのメイン処理"""
    # 1〜100の間の整数をランダムに選択
    target_number = random.randint(1, 100)
    
    # 試行回数をカウントする変数を初期化
    attempts = 0
    
    print("=== 数当てゲーム ===")
    print("1〜100の間の整数を当ててください！")
    print()
    
    # 正解するまで繰り返す
    while True:
        try:
            # ユーザーから数値を入力してもらう
            user_input = input("数値を入力してください: ")
            
            # 文字列を整数に変換
            guess = int(user_input)
            
            # 試行回数を1増やす
            attempts += 1
            
            # 入力値が1〜100の範囲外の場合
            if guess < 1 or guess > 100:
                print("1〜100の間の数値を入力してください。")
                continue
            
            # 入力値と正解を比較して判定
            if guess < target_number:
                # 入力値が小さい場合は「もっと大きい」と表示
                print("もっと大きい")
            elif guess > target_number:
                # 入力値が大きい場合は「もっと小さい」と表示
                print("もっと小さい")
            else:
                # 正解した場合
                print(f"正解です！答えは {target_number} でした。")
                print(f"試行回数: {attempts} 回")
                break  # ゲーム終了
                
        except ValueError:
            # 数字以外が入力された場合の例外処理
            print("エラー: 数値を入力してください。")
            # 試行回数はカウントしない（continueで次のループへ）
        except Exception as e:
            # その他の予期しないエラーが発生した場合
            print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
