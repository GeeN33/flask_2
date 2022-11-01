from flask import Flask, request, render_template

app = Flask(__name__)

list_users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

@app.route('/users/')
def users():
    term = request.args.get('term')
    if term is None : term=''
    return render_template(
        'users/index.html',
        list_users=list_users,
        search=term,
    )

@app.route('/users_id/<id>')
def users_id(id):
    return render_template(
        'users/show.html',
        id=id
    )


if __name__ == '__main__':
    app.run(debug=True)



