from django.shortcuts import render, redirect
import qrcode
from .models import Code

# Create your views here.
def render_create_code(request):
    empty_inputs_error = False
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
        user = request.user
        print("user =", user)
        Code.objects.create(
            image_qr = image_path,
            title = title,
            url = url,
            creator = user,
            description = description
        )
        return redirect('/create_code/')
    return render(
        request = request,
        template_name = "create_code.html",
        context = {
            'authenticated': request.user.is_authenticated,
            "empty_inputs_error": empty_inputs_error
        }
    )