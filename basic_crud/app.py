from flask import Flask,render_template,request,redirect,url_for
ma=Flask(__name__)
student_list = [{"Name":"Sivapackia","Age":22 ,"RollNo": 101, "Marks":[90,75,80,98,65]},
                    {"Name":"Siva","Age":21 ,"RollNo": 102, "Marks":[90,75,80,78,99]},
                    {"Name":"Vilobin","Age":21 ,"RollNo": 103, "Marks":[94,75,80,88,35]},
                    {"Name":"Mahadevi","Age":27 ,"RollNo": 104, "Marks":[70,85,80,98,35]},          
                    {"Name":"Nisha","Age":23 ,"RollNo": 105, "Marks":[90,75,85,98,35]},
                    {"Name":"Vaisali","Age":27 ,"RollNo": 106, "Marks":[80,98,35,90,75]},
                    {"Name":"Vijay","Age":22 ,"RollNo": 107, "Marks":[90,80,98,35,75]},
                    {"Name":"Mohamed Ismail","Age":22 ,"RollNo": 108, "Marks":[75,80,90,98,35]},
                    ]
student_info=[]
@ma.route("/",methods=["GET","POST"])
def user():
    if request.method=="POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        RollNo=request.form.get("RollNo")
        mark1=request.form.get("mark1")
        mark2=request.form.get("mark2")
        mark3=request.form.get("mark3")
        mark4=request.form.get("mark4")
        mark5=request.form.get("mark5")
        Mark_list=[]
        Mark_list.append(mark1)
        Mark_list.append(mark2)
        Mark_list.append(mark3)
        Mark_list.append(mark4)
        Mark_list.append(mark5)
        student_dict={}
        student_dict.update({"Name":Name})
        student_dict.update({"Age":Age})
        student_dict.update({"RollNo":RollNo})
        student_dict.update({"Marks":Mark_list})
        student_info.append(student_dict)
        return render_template("index.html",data=student_info,student=student_list)
    return render_template("index.html",data=student_info,student=student_list)
@ma.route('/edit/<int:index>',methods=["GET","POST"])
def edit(index):
       if request.method=="POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        RollNo=request.form.get("RollNo")
        mark1=request.form.get("mark1")
        mark2=request.form.get("mark2")
        mark3=request.form.get("mark3")
        mark4=request.form.get("mark4")
        mark5=request.form.get("mark5")
        Marks=[mark1,mark2,mark3,mark4,mark5]
        vj=student_list[index-1]
        vj["Name"]=Name
        vj["Age"]=Age
        vj["RollNo"]=RollNo
        vj["Marks"]=Marks
        return redirect(url_for("user"))
       student_edit=student_list[index-1]
       return render_template("edit.html",student=student_edit)
@ma.route("/delete/<int:index>",methods=["GET","POST"])
def delete(index):
    student_list.pop(index-1)
    return render_template("index.html",methods=["GET","POST"])

if __name__=="__main__":
    ma.run(debug=True)
