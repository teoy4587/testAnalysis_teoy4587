from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt

diabetes = load_diabetes()

df_exp = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
df_target = pd.DataFrame(diabetes.target,columns=["target"])

df = pd.concat([df_exp, df_target], axis=1)

df.rename({"s1":"tc", "s2":"LDL","s3":"HDL","s6":"BloodGlucose"},axis=1,inplace=True)
df.dropna(inplace=True)

#plt.plot(df["age"], df["target"])
plt.plot([1,2,3,4], [3,6,9,9])
plt.show()

#fig = plt.gifure(figsize=(5, 5))


