from django.shortcuts import render, redirect
import qrcode, os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from django.contrib.auth.decorators import login_required
from .models import Code
from PIL import Image


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# Create your views here.
@login_required
def render_create_code(request):

    code = False
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        color = request.POST.get("color")
        bg_color = request.POST.get("bg_color")
        embaded_img = request.FILES.get("center_image")
        version = request.POST.get("version")
        radius = request.POST.get("radius")

        print(title, "\n", url, "\n", description, "\n", color, "\n", bg_color, "\n", embaded_img, "\n", radius)

        folder_path = f"media/{request.user}"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        qrcode_image_path = f'{folder_path}/{title}.png'
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
            image_factory = StyledPilImage,
            eye_drawer = RoundedModuleDrawer(radius_ratio = float(radius)),
            module_drawer = RoundedModuleDrawer(radius_ratio = float(radius)),
            color_mask = SolidFillColorMask(back_color = hex_to_rgb(bg_color), front_color = hex_to_rgb(color)),
        )
        if embaded_img:
            center_iamge = Image.open(embaded_img).resize((75, 75), Image.LANCZOS)
            offset = ((image.size[0] - 75) // 2, (image.size[1] - 75) // 2)
            image.paste(center_iamge, offset, mask = center_iamge.split()[3] if center_iamge == "RGBA" else None)
        image.save(qrcode_image_path)
        user = request.user
        print("user =", user)

        code = Code.objects.create(
            image_qr = f'{request.user}/{title}.png',
            title = title,
            url = url,
            creator = user,
            description = description,
            color = color,
            bgcolour = bg_color, 
            costomization = radius,
            center_image = embaded_img
            )

        cur_code = Code.objects.last()
        cur_date_time = str(cur_code.date_time)
        date_time_change = int(cur_date_time.split(' ')[-1].split(":")[0])+2

        step1 = cur_date_time.split(' ')[0]
        # print(step1)
        step2 = cur_date_time.split(":")[1] + ":" + cur_date_time.split(":")[2] + ":" + cur_date_time.split(":")[3]
        # print(step2)
        step3 = step1 + " " + str(date_time_change) + ":" + step2
        # print(step3)
        code.date_time = step3
        code.save()
        print("code.image_qr =", code.image_qr)
    return render(
        request = request,
        template_name = "create_code.html",
        context = {
            'authenticated': request.user.is_authenticated,
            "code": code
        }
    )