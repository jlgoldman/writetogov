from PIL import Image

from database import db_models

def main():
    base_img_master = Image.open('resources/rep-social-image-background.jpg')
    for db_rep in db_models.Rep.query:
        if db_rep.first_name:
            base_img = base_img_master.copy()
            rep_img = Image.open('data/rep_images/%d.jpg' % db_rep.rep_id)
            yoffset = (base_img.size[1] - rep_img.size[1]) / 2
            offset = (yoffset, yoffset)
            base_img.paste(rep_img, offset)
            base_img.save('data/rep_images/social/%d-social.jpg' % db_rep.rep_id)

if __name__ == '__main__':
    from tools import db_utils
    with db_utils.request_context():
        main()
