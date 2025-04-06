import pandas as pd
import pickle
import statsmodels.api as sm

# excelの読み込み
df = pd.read_excel("data_results.xlsx")

# 説明変数の設定
X = df[["Vo","Da","Vi"]]
# 目的変数の設定
Y = df[["結果値"]]

X = sm.add_constant(X)

# 重回帰モデルの作成
model=sm.OLS(Y,X).fit()

with open("model.pkl","wb") as f:
    pickle.dump(model,f)

# モデル作成結果をcsvファイルで出力
summary_txt=model.summary().as_text()
# 作成結果の文字列を改行で分割しリスト化
summary_lines=summary_txt.split("\n")
# 作成結果のリストをデータフレーム化
summary_df=pd.DataFrame(summary_lines)
# 作成結果のcsvファイルとして出力
summary_df.to_csv("summary.csv",index=False,header=False,encoding="utf-8-sig")