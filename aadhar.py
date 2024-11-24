from flask import Flask, request, render_template


aadhar=Flask(__name__)
@aadhar.route('/')
def form():
    return render_template('Apan.html')

@aadhar.route('/upload', methods=['POST'])
def verify():
    MAX=50*1024*1024
    a = request.files['file']
    
    if a and len(a.read()) > MAX:
        a.seek(0)
        return render_template('notok.html')

    return render_template('okaadhar.html')

if __name__ =="__main__":
    aadhar.run(debug=True)

    