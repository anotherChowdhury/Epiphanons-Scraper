from flask import Flask, jsonify, request, make_response
from scraper import get_data

app = Flask(__name__)


@app.route('/', methods=["GET"])
def respond():
    print(request.args)
    if(not request.args):
        response_object = {
            "name": "Aaqib Farhan Hossain", "posted_at": "1 October at 07:49", "post_link": "https://www.facebook.com/aaqib.hossain/posts/10164207311055109", "profile_link": "https://www.facebook.com/aaqib.hossain/", "post": "There's an unsettling spike in the documentation of reported sexual assault in this country during this lockdown period(its always been high but undocumented).\nWhat I'm seeing as a response to this is far too much content on how rapists should be treated, and not enough content on how rape survivors should be treated.\nFocus on the latter topic.", "image": "https://scontent.fdac9-1.fna.fbcdn.net/v/t1.0-1/p720x720/119450452_10164149725720109_8990952581758453891_o.jpg?_nc_cat=105&_nc_sid=dbb9e7&_nc_ohc=2Prp3gMtc1gAX9rLEvZ&_nc_ht=scontent.fdac9-1.fna&tp=6&oh=55c75f9f6ff3ef4a39bf50572973f71f&oe=5FA71ED4"
        }
        return make_response(jsonify({
            "message": "This is an endpoint for scraping a public facebook post. It will respond with post's owners name,profile link,profile picture,post time and post text",
            "method": "GET",
            "requestExample": "?url=https://www.facebook.com/aaqib.hossain/posts/10164207311055109",
            "resposne": response_object
        }))
    return make_response(jsonify(get_data(request.args.get('url'))))


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)
