from flask import Flask, jsonify, request, make_response
from scraper import get_data

app = Flask(__name__)


@app.route('/', methods=["GET"])
def respond():
    print(request.args)
    if(not request.args):
        response_object = {
            "name": "Niamul Karim Rafi", "time": "2020-10-12T00:54:00", "postLink": "https://www.facebook.com/niamul.karimarrafi.7/posts/645105246366409", "profileLink": "https://www.facebook.com/niamul.karimarrafi.7", "text": 'খুলনার টপ রেটেড খাটি চুই ঝাল এনে দিচ্ছি। কেজি প্রতি ৫০০ টাকা করে। কেউ নিলে জানাতে পারেন 😃', "image": "https://scontent.fdac9-1.fna.fbcdn.net/v/t1.0-1/p720x720/121058659_643947316482202_2920325133192565030_o.jpg?_nc_cat=106&_nc_sid=dbb9e7&_nc_ohc=10CUjSPskS8AX-12eJW&_nc_ht=scontent.fdac9-1.fna&tp=6&oh=968b16629bb6a7b15d5e39a9043cc451&oe=5FAC7B00"
        }
        return make_response(jsonify({
            "message": "This is an endpoint for scraping a public facebook post. It will respond with post's owners name,profile link,profile picture,post time and post text",
            "method": "GET",
            "requestExample": "https://scrapelink.herokuapp.com?url=https://www.facebook.com/niamul.karimarrafi.7/posts/645105246366409",
            "resposne": response_object
        }))
    return make_response(jsonify(get_data(request.args.get('url'))))


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)
