import io
import sys
import unittest
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter

# Rest of your route definitions...

if __name__ == '__main__':
    app.run(port=5555)

# Define your test class as a subclass of unittest.TestCase
class TestApp(unittest.TestCase):

    def test_print_text_in_console(self):
        '''displays text of route in console.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        with app.app_context():
            app.test_client().get('/print/some_string')
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == 'some_string\n'

if __name__ == '__main__':
    unittest.main()
