from django.shortcuts import render, HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("<H1>Hello World, This is my First Web </H1>"
                        "<H2>I Love Girls' Generation, It's My Life</H2>")

def firstPage(request):
    return render(request, 'FirstPage.html')

def secondpage(request):
    return render(request, 'SecondPage.html')

def thirdpage(request):
    return render(request, 'thirdpage.html')

def hnypage(request):
    return render(request, 'hnypage.html')

def home(request):
    return render(request, 'home.html')

def myData(request):
    name = "Mr. Banthat"
    surname = "Upara"
    gender = "Male"
    education = "ปรัญญาตรี ปีที่ 3"
    status = "Student"
    work = "RMUTI"
    return render(request, 'myData.html',
                  {'name': name, 'surname': surname, 'gender': gender,
                   'education': education, 'status': status, 'work': work})


    # context = {'name': name, 'surname': surname, 'gender': gender,
    #            'education': education, 'status': status, 'work': work}
    # return render(request, 'myData.html', context)

def showMyData(request):
    showID = "65342310264-8"
    showName = "นายบัณทัต อุประ"
    showAddress = "46 หมู่ 8 ตำบลแคนใหญ่ อำเภอเมืองร้อยเอ็ด จังหวัดร้อยเอ็ด 45000"
    showTel = "0855129238"
    showGender = "ชาย"
    showBirthday = "12 กุมภาพันธ์ 2545"
    showWeight = 45
    showHeight = 169
    showStatus = "นักศึกษา"
    showSchool = "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น"

    products = []

    product = ['บุรุษเต้าหู้สะท้านภพ', 450.00, '../../static/images/book_1.gif']
    products.append(product)
    product = ['ก็จะดื้อ (2 เล่มจบ)', 559.00, '../../static/images/book_2.gif']
    products.append(product)
    product = ['วันๆ ของจิ้งจอกลูกสองก็แบบนี้แหละ!', 429.00, '../../static/images/book_3.gif']
    products.append(product)
    product = ['A piece of cake', 289.00, '../../static/images/book_4.gif']
    products.append(product)
    product = ['ทีเร็กซ์จะไม่ดื้อ', 399.00, '../../static/images/book_5.gif']
    products.append(product)
    product = ['บุรุษเต้าหู้สะท้านภพ', 450.00, '../../static/images/book_6.gif']
    products.append(product)
    product = ['นับสิบจะจูบ (2 เล่มจบ)', 680.00, '../../static/images/book_7.gif']
    products.append(product)
    product = ['เกิดใหม่เป็นตัวร้ายผู้รักสงบ', 379.00, '../../static/images/book_8.gif']
    products.append(product)
    product = ['ผมไม่เป็น(โอเมก้า)ของคุณหรอก! (3 เล่มจบ)', 948.00, '../../static/images/book_11.gif']
    products.append(product)
    product = ['Real Alpha (2 เล่มจบ)', 518.00, '../../static/images/book_10.gif']
    products.append(product)

    context = {'showID': showID, 'showName': showName, 'showAddress': showAddress, 'showTel': showTel,
               'showGender': showGender, 'showBirthday': showBirthday, 'showWeight': showWeight,
               'showHeight': showHeight, 'showStatus': showStatus, 'showSchool': showSchool, 'products': products}

    return render(request, 'showMyData.html', context)
