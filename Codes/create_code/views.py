from django.shortcuts import render
import qrcode

# Create your views here.
def render_create_code(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        print(title, "\n", url, "\n", description)
        
        qrcodes_folder_path = __file__.split("/")
        del qrcodes_folder_path[-1]
        qrcodes_folder_path = "/".join(qrcodes_folder_path) + "/media/qrcodes"
        print("qrcodes_folder_path =", qrcodes_folder_path)
        qr = qrcode.QRCode(
            version = 2,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 15,
            border = 2
        )
        qr.add_data(url)
        qr.make(fit = True)
        image = qr.make_image()
        image.save(f'{qrcodes_folder_path}/QRCode.png')
    return render(
        request = request,
        template_name = "create_code.html",
        context = {
            'authenticated': request.user.is_authenticated
        }
    )