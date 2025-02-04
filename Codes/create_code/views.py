from django.shortcuts import render, redirect
import qrcode
from .models import Code

# Create your views here.
def render_create_code(request):
    empty_inputs_error = False
    anonimus_user_error = False
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        print(title, "\n", url, "\n", description)
        
        qrcodes_folder_path = __file__.split("/")
        del qrcodes_folder_path[-1]
        qrcodes_folder_path = "/".join(qrcodes_folder_path) + "/media/qrcodes"
        image_path = f'{qrcodes_folder_path}/{title}.png'
        qr = qrcode.QRCode(
            version = 2,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 15,
            border = 2
        )
        try:
            qr.add_data(url)
            qr.make(fit = True)
            image = qr.make_image()
            image.save(image_path)
        except:
            print("error")
            empty_inputs_error = True
        try:
            user = request.user
            print("user =", user)
            Code.objects.create(
                image_qr = image_path,
                title = title,
                url = url,
                creator = user,
                description = description
            )
        except:
            anonimus_user_error = True
        print("last obj =", Code.objects.last())
        cur_code = Code.objects.last()
        cur_date_time = str(cur_code.date_time)
        date_time_change = int(cur_date_time.split(' ')[-1].split(":")[0])+2
        num = "151"
        print("num =", num.split("5")) # num = 5 5 5
        print("cur_date_time =", cur_date_time )
        print(date_time_change)
        step1 = cur_date_time.split(' ')[0]
        print(step1)
        step2 = cur_date_time.split(":")[1] + ":" + cur_date_time.split(":")[2] + ":" + cur_date_time.split(":")[3]
        print(step2)
        step3 = step1 + " " + str(date_time_change) + ":" + step2
        print(step3)
        Code.objects.last().date_time = step3
        return redirect('/create_code/')
    return render(
        request = request,
        template_name = "create_code.html",
        context = {
            'authenticated': request.user.is_authenticated,
            "empty_inputs_error": empty_inputs_error,
            "anonimus_user_error": anonimus_user_error
        }
    )