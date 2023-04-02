import yagmail


yag_server = yagmail.SMTP(
    user="xxx@yyy.cn",
    password="123456",
    host="smtp.xxx.yyy.cn",
)

email_to = [
    "123456@sina.com",
    "123456@qq.com",
]
email_title = "This is a test"
# email_content = "some content"
email_content = r"./cv.html"
email_attachments = [
    "./cv.html",
    "./emailSender.py",
]

res = yag_server.send(email_to, email_title, email_content, email_attachments)
with open("./email-log.txt", mode="a", encoding="utf-8") as file_obj:
    file_obj.write("Title: " + email_title + "\n")
    file_obj.write("Content: " + email_content + "\n")
    file_obj.write("Reslt: " + str(res) + "\n")
    file_obj.write("To: ")
    for i in range(len(email_to)):
        file_obj.write(str(email_to[i]) + ",")
    for i in range(len(email_attachments)):
        file_obj.write("Attachment(" + str(i) + ")" + str(email_attachments[i]) + "\n")
    print("Sent")

yag_server.close()


###################################################################################
###################################################################################
# send_times = 1
# email_interval = 60*60*2.5
# for i in range(send_times):
#     yag_server.send(email_to, email_title, email_content, email_attachments)
#     print("Sent!")
#     time.sleep((0, 3)[send_times==1])
