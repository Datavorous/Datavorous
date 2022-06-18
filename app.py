from flask import Flask, render_template,Markup
import utils
import markdown

app = Flask(__name__)

@app.route("/")
def index():
	files = utils.file_list()
	metadata = []
	for i in range(len(files)):metadata.append(utils.get_meta(i))
	metadata = utils.sort(metadata)
	return render_template("index.html",
		no_posts=len(files),
		contents=metadata)


@app.route("/posts/<int:post_no>")
def show_post(post_no):
	file = open(f"posts/{utils.file_list()[post_no-1]}","r")
	html = utils.get_content(file)
	file.close()
	return render_template("posts.html",contents=[Markup(html),utils.get_meta(post_no-1)])


if __name__ == "__main__":
	app.run(debug=True)
