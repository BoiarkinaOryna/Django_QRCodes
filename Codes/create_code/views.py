from django.shortcuts import render, redirect
import qrcode, os
from qrcode.image.styledpil import StyledPilImage
from django.core.files.storage import FileSystemStorage
from .models import Code
from PIL import Image

# Create your views here.
def render_create_code(request):
    # empty_inputs_error = False
    anonimus_user_error = False
    code = False
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        color = request.POST.get("color")
        bg_color = request.POST.get("bg_color")
        embaded_img = request.FILES.get("center_image")
        version = request.POST.get("version")

        print(title, "\n", url, "\n", description, "\n", color, "\n", bg_color, "\n", embaded_img)
        
        qrcodes_folder_path = __file__.split("/")
        del qrcodes_folder_path[-1]
        qrcodes_folder_path = "/".join(qrcodes_folder_path) + "/media/qrcodes"
        qrcode_image_path = f'{qrcodes_folder_path}/{title}.png'
        qr = qrcode.QRCode(
            version = version,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 15,
            border = 2
        )
        # try:
        qr.add_data(url)
        qr.make(fit = True)
        image = qr.make_image(
            # image_factory = StyledPilImage,
            # embeded_image_path = embaded_img,
            fill_color = color,
            back_color = bg_color,
        )
        if embaded_img:
            center_iamge = Image.open(embaded_img).resize((75, 75), Image.LANCZOS)
            offset = ((image.size[0] - 75) // 2, (image.size[1] - 75) // 2)
            image.paste(center_iamge, offset, mask = center_iamge.split()[3] if center_iamge == "RGBA" else None)
        image.save(qrcode_image_path)

        short_path_to_image = os.path.join("media", "qrcodes", f"{title}.png")
        # fss = FileSystemStorage()
        # print("short_path_to_image type =", type(short_path_to_image), "\n", "image type =", type(image))
        # fss.save(
        #     name = short_path_to_image,
        #     content = image
        # )
        
        # except:
        #     print("empty_inputs_error")
        #     empty_inputs_error = True
        
        try:
            user = request.user
            print("user =", user)
            code = Code.objects.create(
                image_qr = short_path_to_image,
                title = title,
                url = url,
                creator = user,
                description = description,
                color = color,
                bgcolour = bg_color
            )
        except:
            print("anonimus_user_error")
            anonimus_user_error = True
        # print("last obj =", Code.objects.last())
        cur_code = Code.objects.last()
        cur_date_time = str(cur_code.date_time)
        date_time_change = int(cur_date_time.split(' ')[-1].split(":")[0])+2
        # print("num =", num.split("5")) # num = 5 5 5
        # print("cur_date_time =", cur_date_time )
        # print(date_time_change)
        step1 = cur_date_time.split(' ')[0]
        # print(step1)
        step2 = cur_date_time.split(":")[1] + ":" + cur_date_time.split(":")[2] + ":" + cur_date_time.split(":")[3]
        # print(step2)
        step3 = step1 + " " + str(date_time_change) + ":" + step2
        # print(step3)
        try:
            code.date_time = step3
            code.save()
            print("code.image_qr =", code.image_qr)
        except:
            anonimus_user_error = True
            print("anonimus_user_error2")
        # return redirect('/create_code/')
    return render(
        request = request,
        template_name = "create_code.html",
        context = {
            'authenticated': request.user.is_authenticated,
            # "empty_inputs_error": empty_inputs_error,
            "anonimus_user_error": anonimus_user_error,
            "code": code
        }
    )