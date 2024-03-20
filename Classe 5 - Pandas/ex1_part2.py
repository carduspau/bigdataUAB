import pandas as pd

df = pd.read_csv("dataset.csv")

average_views = df["viewCount"].mean()
average_comments = df["commentCount"].mean()
average_likes = df["likeCount"].mean()

df["desviacio_likes_total"] = df["likeCount"] - average_likes
df["desviacio_likes_percentual"] = (df["likeCount"] - average_likes) / average_likes * 100

df["desviacio_comments_total"] = df["commentCount"] - average_comments
df["desviacio_comments_percentual"] = (df["commentCount"] - average_comments) / average_comments * 100

df["desviacio_views_total"] = df["viewCount"] - average_views
df["desviacio_views_percentual"] = (df["viewCount"] - average_views) / average_views * 100

max_view = df[df["viewCount"] == df["viewCount"].max()]
print(max_view)

max_comment = df[df["commentCount"] == df["commentCount"].max()]
print(max_comment)

df = df.drop(["channelId","categoryId","channelTitle","tags","publishedAt","blocked_at"], axis=1)

df.to_csv("noves_dades.csv", index=False, sep=";")
