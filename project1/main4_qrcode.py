import qrcode

qr_data = 'github.com/quasar529/python_mini_projects'
qr_img = qrcode.make(qr_data)

save_path = 'project1\\' + qr_data + '.png'
qr_img.save(save_path)
