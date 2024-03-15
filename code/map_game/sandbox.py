QPixmap pixmap("image_path");
QIcon ButtonIcon(pixmap);
button->setIcon(ButtonIcon);
button->setIconSize(pixmap.rect().size());