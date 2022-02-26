def upload_image(instance, filename):
    return "static/tokens/img/{}/{}/{}".format(instance.raised_by,instance.id, filename)