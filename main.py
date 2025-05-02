import requests

# 取得したいAPIのURL
url = "https://jsonplaceholder.typicode.com/posts"

# APIにGETリクエストを送る
response = requests.get(url)

# レスポンス（返答）が成功しているか確認
if response.status_code == 200:
    # 返ってきたデータをJSON形式で取得
    posts = response.json()

    # 取得した記事データの一部を表示してみる
    for post in posts[:5]:  # 最初の5件だけ表示
        print(f"タイトル: {post['title']}")
        print(f"本文: {post['body']}\n")
else:
    print(f"エラーが発生しました！ ステータスコード: {response.status_code}")
