import os
from PyQt6 import QtWidgets, QtGui
from countries_information import Country


class InteractiveMap(QtWidgets.QWidget):
    """
    The interactive map for the player to study the map before (or after) playing the game. When a country on a map is
    clicked on, an information window pops up and shows the info that will be needed for the game.
    """
    def __init__(self):
        super().__init__()

        self.bg_map_path = "GUI_items/interactive_map/europe_map_bg.png"
        self.maps_folder = "GUI_items/interactive_map/countries"
        self.countries_paths = []
        for file in os.listdir(self.maps_folder):
            country_path = os.path.join(self.maps_folder, file)
            if ".png" in country_path:  # MacOS can create a .DS_Store file into the directory. Ignore it
                self.countries_paths.append(country_path)

        self.map_label = QtWidgets.QLabel(self)
        self.map_image = QtGui.QPixmap(self.bg_map_path)
        self.map_image = self.map_image.scaledToHeight(500)
        self.map_label.setPixmap(self.map_image)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.map_label)
        self.setLayout(self.layout)

    def mousePressEvent(self, mouse_event):
        # Handle mouse click events. PyQT creates the event object automatically, so I don't have to create it.
        x = mouse_event.position().x()
        y = mouse_event.position().y()

        # Determine which region was clicked based on mouse coordinates
        clicked_region = self.get_clicked_region(x, y)

        # Highlight the clicked region
        self.highlight_region(clicked_region)

        # Display information about the clicked region
        self.display_region_info(clicked_region)

    def get_clicked_region(self, x, y):
        # Determine the region or country based on mouse coordinates
        # This is an incredibly janky way of doing this, but couldn't figure out a better one
        fin_coords = [range(350, 410), range(115, 245)]
        swe_coords = [range(290, 340), range(120, 305)]
        nor_coords = [range(250, 280), range(209, 280)]
        rus_coords = [range(450, 640), range(105, 365)]
        est_coords = [range(370, 385), range(270, 280)]
        lat_coords = [range(352, 385), range(295, 305)]
        den_coords = [range(252, 275), range(302, 320)]
        lit_coords = [range(350, 377), range(311, 330)]
        bel_coords = [range(379, 415), range(325, 355)]
        pol_coords = [range(305, 345), range(340, 375)]
        ukr_coords = [range(375, 460), range(370, 400)]
        mol_coords = [range(395, 405), range(370 + 35, 385 + 35)]  # Made a bit of an oopsie, fix with +35
        rom_coords = [range(355, 390), range(375 + 35, 405 + 35)]
        ser_coords = [range(340, 350), range(400 + 35, 418 + 35)]
        bul_coords = [range(365, 390), range(415 + 35, 430 + 35)]
        nom_coords = [range(347, 356), range(430 + 35, 440 + 35)]
        kos_coords = [range(345, 350), range(420 + 35, 430 + 35)]
        gre_coords = [range(345, 380), range(440 + 35, 495 + 35)]
        tur_coords = [range(395, 505), range(435 + 35, 485 + 35)]
        alb_coords = [range(335, 345), range(435 + 35, 445 + 35)]
        mon_coords = [range(330, 337), range(420 + 35, 428 + 35)]
        bos_coords = [range(319, 330), range(405 + 35, 418 + 35)]
        cro_coords = [range(300, 325), range(390 + 35, 410 + 35)]
        slo_coords = [range(295, 310), range(388 + 35, 395 + 35)]
        hun_coords = [range(315, 350), range(372 + 35, 385 + 35)]
        slova_coords = [range(320, 348), range(358 + 35, 365 + 35)]
        cze_coords = [range(290, 319), range(343 + 35, 357 + 35)]
        ger_coords = [range(245, 287), range(304 + 35, 365 + 35)]
        aus_coords = [range(286, 309), range(367 + 35, 380 + 35)]
        swi_coords = [range(245, 262), range(377 + 35, 386 + 35)]
        net_coords = [range(225, 239), range(316 + 35, 329 + 35)]
        ita_coords = [range(257, 307), range(390 + 35, 473 + 35)]
        belg_coords = [range(222, 236), range(338 + 35, 345 + 35)]
        fra_coords = [range(168, 237), range(347 + 35, 411 + 35)]
        spa_coords = [range(151, 183), range(419 + 35, 469 + 35)]
        por_coords = [range(130, 140), range(437 + 35, 472 + 35)]
        uk_coords = [range(153, 201), range(247 + 35, 335 + 35)]
        ire_coords = [range(124, 150), range(305 + 35, 323 + 35)]
        ice_coords = [range(21, 94), range(122 + 35, 167 + 35)]

        if x in fin_coords[0] and y in fin_coords[1]:
            return "finland"
        elif x in swe_coords[0] and y in swe_coords[1]:
            return "sweden"
        elif x in nor_coords[0] and y in nor_coords[1]:
            return "norway"
        elif x in rus_coords[0] and y in rus_coords[1]:
            return "russia"
        elif x in est_coords[0] and y in est_coords[1]:
            return "estonia"
        elif x in lat_coords[0] and y in lat_coords[1]:
            return "latvia"
        elif x in den_coords[0] and y in den_coords[1]:
            return "denmark"
        elif x in lit_coords[0] and y in lit_coords[1]:
            return "lithuania"
        elif x in bel_coords[0] and y in bel_coords[1]:
            return "belarus"
        elif x in pol_coords[0] and y in pol_coords[1]:
            return "poland"
        elif x in ukr_coords[0] and y in ukr_coords[1]:
            return "ukraine"
        elif x in mol_coords[0] and y in mol_coords[1]:
            return "moldova"
        elif x in rom_coords[0] and y in rom_coords[1]:
            return "romania"
        elif x in ser_coords[0] and y in ser_coords[1]:
            return "serbia"
        elif x in bul_coords[0] and y in bul_coords[1]:
            return "bulgaria"
        elif x in nom_coords[0] and y in nom_coords[1]:
            return "north macedonia"
        elif x in kos_coords[0] and y in kos_coords[1]:
            return "kosovo"
        elif x in gre_coords[0] and y in gre_coords[1]:
            return "greece"
        elif x in tur_coords[0] and y in tur_coords[1]:
            return "turkey"
        elif x in alb_coords[0] and y in alb_coords[1]:
            return "albania"
        elif x in mon_coords[0] and y in mon_coords[1]:
            return "montenegro"
        elif x in bos_coords[0] and y in bos_coords[1]:
            return "bosnia and herzegovina"
        elif x in cro_coords[0] and y in cro_coords[1]:
            return "croatia"
        elif x in slo_coords[0] and y in slo_coords[1]:
            return "slovenia"
        elif x in hun_coords[0] and y in hun_coords[1]:
            return "hungary"
        elif x in slova_coords[0] and y in slova_coords[1]:
            return "slovakia"
        elif x in cze_coords[0] and y in cze_coords[1]:
            return "czechia"
        elif x in ger_coords[0] and y in ger_coords[1]:
            return "germany"
        elif x in aus_coords[0] and y in aus_coords[1]:
            return "austria"
        elif x in swi_coords[0] and y in swi_coords[1]:
            return "switzerland"
        elif x in net_coords[0] and y in net_coords[1]:
            return "netherlands"
        elif x in ita_coords[0] and y in ita_coords[1]:
            return "italy"
        elif x in belg_coords[0] and y in belg_coords[1]:
            return "belgium"
        elif x in fra_coords[0] and y in fra_coords[1]:
            return "france"
        elif x in spa_coords[0] and y in spa_coords[1]:
            return "spain"
        elif x in por_coords[0] and y in por_coords[1]:
            return "portugal"
        elif x in uk_coords[0] and y in uk_coords[1]:
            return "united kingdom"
        elif x in ire_coords[0] and y in ire_coords[1]:
            return "ireland"
        elif x in ice_coords[0] and y in ice_coords[1]:
            return "iceland"

    def highlight_region(self, region):
        # Change the appearance of the clicked region to indicate selection
        for path in self.countries_paths:
            if region is not None and region in path:
                image = QtGui.QPixmap(self.countries_paths[self.countries_paths.index(path)])
                image = image.scaledToHeight(500)
                self.map_label.setPixmap(image)

    def display_region_info(self, region):
        # Display information about the clicked region
        info_box = QtWidgets.QMessageBox(self)
        icon = QtGui.QPixmap("GUI_items/info_icon.png")

        for path in self.countries_paths:
            if region is not None and region in path:
                info_box.setIconPixmap(icon)
                info_box.setText(region.capitalize())
                info_box.setInformativeText(Country(region).__str__())
                info_box.exec()


