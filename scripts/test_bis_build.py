import json
import unittest
import bis_build

class TestBISBuildLength(unittest.TestCase):

    def setUp(self):
        self.json_file1 = open('src/json/itemWinUsage.json', 'r')
        self.itemUsageDict = json.load(self.json_file1)
        self.json_file2 = open('src/json/item.json', 'r')
        self.items = json.load(self.json_file2)
        self.currentBuild = set()

    def tearDown(self) -> None:
        self.json_file1.close()
        self.json_file2.close()
        

    def test_aatrox(self):
        buildAatrox = bis_build.generate_build(self.items["data"], self.itemUsageDict, "Aatrox", self.currentBuild)
        self.assertEqual(len(buildAatrox), 6)

    def test_ahri(self):
        buildAhri = bis_build.generate_build(self.items["data"], self.itemUsageDict, "Ahri", self.currentBuild)
        self.assertEqual(len(buildAhri), 6)

    def test_akali(self):
        buildAkali = bis_build.generate_build(self.items["data"], self.itemUsageDict, "Akali", self.currentBuild)
        self.assertEqual(len(buildAkali), 6)

    def test_alistar(self):
        buildAlistar = bis_build.generate_build(self.items["data"], self.itemUsageDict, "Alistar", self.currentBuild)
        self.assertEqual(len(buildAlistar), 6)


    def test_amumu(self):
        buildAmumu = bis_build.generate_build(self.items["data"], self.itemUsageDict, "Amumu", self.currentBuild)
        self.assertEqual(len(buildAmumu), 6)

    
    def test_anivia(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Anivia", self.currentBuild)), 6)

    def test_annie(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Annie", self.currentBuild)), 6)

    def test_aphelios(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Aphelios",self.currentBuild)), 6)

    def test_ashe(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Ashe", self.currentBuild)), 6)

    def test_aurelion_sol(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "AurelionSol", self.currentBuild)), 6)

    def test_azir(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Azir", self.currentBuild)), 6)

    def test_bard(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Bard", self.currentBuild)), 6)

    def test_blitzcrank(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Blitzcrank",self.currentBuild)), 6)

    def test_brand(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Brand",self.currentBuild)), 6)
    
    def test_braum(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Braum", self.currentBuild)), 6)

    def test_caitlyn(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Caitlyn", self.currentBuild)), 6)

    def test_camille(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Camille", self.currentBuild)), 6)

    def test_cassiopeia(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Cassiopeia", self.currentBuild)), 6)

    def test_cho_gath(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Chogath", self.currentBuild)), 6)

    def test_corki(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Corki", self.currentBuild)), 6)

    def test_darius(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Darius", self.currentBuild)), 6)

    def test_diana(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Diana", self.currentBuild)), 6)

    def test_dr_mundo(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "DrMundo", self.currentBuild)), 6)

    def test_draven(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Draven", self.currentBuild)), 6)

    def test_ekko(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Ekko", self.currentBuild)), 6)
    
    def test_elise(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Elise", self.currentBuild)), 6)
    
    def test_evelynn(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Evelynn", self.currentBuild)), 6)

    def test_ezreal(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Ezreal", self.currentBuild)), 6)

    def test_fiddlesticks(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "FiddleSticks", self.currentBuild)), 6)

    def test_fiora(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Fiora", self.currentBuild)), 6)

    def test_fizz(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Fizz", self.currentBuild)), 6)

    def test_galio(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Galio", self.currentBuild)), 6)

    def test_gangplank(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Gangplank", self.currentBuild)), 6)

    def test_garen(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Garen",self.currentBuild)), 6)

    def test_gnar(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Gnar", self.currentBuild)), 6)

    def test_gragas(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Gragas", self.currentBuild)), 6)

    def test_graves(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Graves", self.currentBuild)), 6)

    def test_gwen(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Gwen", self.currentBuild)), 6)

    def test_hecarim(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Hecarim",self.currentBuild)), 6)

    def test_heimerdinger(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Heimerdinger", self.currentBuild)), 6)

    def test_illaoi(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Illaoi", self.currentBuild)), 6)

    def test_irelia(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Irelia", self.currentBuild)), 6)

    def test_ivern(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Ivern", self.currentBuild)), 6)

    def test_janna(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Janna", self.currentBuild)), 6)

    def test_jarvan(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "JarvanIV", self.currentBuild)), 6)

    def test_jax(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Jax", self.currentBuild)), 6)
    
    def test_jayce(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Jayce", self.currentBuild)), 6)

    def test_jhin(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Jhin", self.currentBuild)), 6)

    def test_jinx(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Jinx", self.currentBuild)), 6)

    def test_kai_sa(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Bard", self.currentBuild)), 6)

    def test_kalista(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Kalista",self.currentBuild)), 6)

    def test_kayn(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Kayn", self.currentBuild)), 6)

    def test_kayle(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Kayle", self.currentBuild)), 6)

    def test_kennen(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Kennen", self.currentBuild)), 6)

    def test_kha_zix(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Khazix", self.currentBuild)), 6)

    def test_kindred(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Kindred", self.currentBuild)), 6)

    def test_kled(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Kled", self.currentBuild)), 6)

    def test_kog_maw(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "KogMaw",self.currentBuild)), 6)

    def test_leblanc(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Leblanc", self.currentBuild)), 6)

    def test_leesin(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "LeeSin", self.currentBuild)), 6)

    def test_leona(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Leona", self.currentBuild)), 6)

    def test_lillia(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Lillia", self.currentBuild)), 6)

    def test_lissandra(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Lissandra", self.currentBuild)), 6)

    def test_lucian(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Lucian", self.currentBuild)), 6)

    def test_lulu(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Lulu", self.currentBuild)), 6)

    def test_lux(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Lux",self.currentBuild)), 6)

    def test_malphite(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Malphite", self.currentBuild)), 6)

    def test_malzahar(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Malzahar", self.currentBuild)), 6)

    def test_maokai(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Maokai", self.currentBuild)), 6)

    def test_master_yi(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "MasterYi", self.currentBuild)), 6)

    def test_miss_fortune(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "MissFortune", self.currentBuild)), 6)

    def test_mordekaiser(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Mordekaiser", self.currentBuild)), 6)

    def test_morgana(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Morgana", self.currentBuild)), 6)

    def test_nami(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Nami",self.currentBuild)), 6)

    def test_nasus(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Nasus",self.currentBuild)), 6)

    def test_nautilus(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Nautilus", self.currentBuild)), 6)

    def test_neeko(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Neeko", self.currentBuild)), 6)

    def test_nidalee(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Nidalee", self.currentBuild)), 6)

    def test_nocturne(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Nocturne", self.currentBuild)), 6)

    def test_nunu(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Nunu",self.currentBuild)), 6)

    def test_olaf(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Olaf", self.currentBuild)), 6)

    def test_orianna(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Orianna",self.currentBuild)), 6)

    def test_ornn(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Ornn", self.currentBuild)), 6)

    def test_pantheon(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Pantheon", self.currentBuild)), 6)

    def test_poppy(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Poppy", self.currentBuild)), 6)

    def test_pyke(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Pyke", self.currentBuild)), 6)

    def test_qiyana(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Qiyana", self.currentBuild)), 6)

    def test_quinn(self):
         self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Quinn", self.currentBuild)), 6)

    def test_rakan(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Rakan", self.currentBuild)), 6)

    def test_rammus(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Rammus",self.currentBuild)), 6)

    def test_rek_sai(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "RekSai",self.currentBuild)), 6)

    def test_rell(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Rell", self.currentBuild)), 6)

    def test_renekton(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Renekton", self.currentBuild)), 6)

    def test_rengar(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Rengar",self.currentBuild)), 6)

    def test_riven(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Riven", self.currentBuild)), 6)

    def test_rumble(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Rumble",self.currentBuild)), 6)
    
    def test_ryze(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Ryze",self.currentBuild)), 6)

    def test_samira(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Samira",self.currentBuild)), 6)

    def test_sejuani(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Sejuani", self.currentBuild)), 6)

    def test_senna(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Senna", self.currentBuild)), 6)

    def test_seraphine(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Seraphine", self.currentBuild)), 6)

    def test_sett(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Sett", self.currentBuild)), 6)

    def test_shaco(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Shaco",self.currentBuild)), 6)

    def test_shen(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Shen", self.currentBuild)), 6)

    def test_shyvana(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Shyvana", self.currentBuild)), 6)

    def test_singed(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Singed",self.currentBuild)), 6)

    def test_sion(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Sion",self.currentBuild)), 6)

    def test_sivir(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Sivir", self.currentBuild)), 6)

    def test_skarner(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Skarner", self.currentBuild)), 6)

    def test_sona(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Sona", self.currentBuild)), 6)

    def test_soraka(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Soraka",self.currentBuild)), 6)

    def test_swain(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Swain", self.currentBuild)), 6)

    def test_sylas(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Sylas", self.currentBuild)), 6)

    def test_syndra(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Syndra", self.currentBuild)), 6)

    def test_tahm_kench(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "TahmKench", self.currentBuild)), 6)

    def test_taliyah(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Taliyah", self.currentBuild)), 6)

    def test_talon(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Talon", self.currentBuild)), 6)

    def test_taric(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Taric",self.currentBuild)), 6)

    def test_teemo(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Teemo",self.currentBuild)), 6)

    def test_thresh(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Thresh",self.currentBuild)), 6)

    def test_tristana(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Tristana", self.currentBuild)), 6)

    def test_trundle(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Trundle", self.currentBuild)), 6)

    def test_tryndamere(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Tryndamere",self.currentBuild)), 6)

    def test_twisted_fate(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "TwistedFate",self.currentBuild)), 6)

    def test_twitch(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Twitch", self.currentBuild)), 6)

    def test_udyr(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Udyr",self.currentBuild)), 6)

    def test_urgot(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Urgot", self.currentBuild)), 6)

    def test_varus(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Varus",self.currentBuild)), 6)

    def test_vayne(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Vayne",self.currentBuild)), 6)

    def test_veigar(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Veigar", self.currentBuild)), 6)

    def test_vel_koz(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Velkoz", self.currentBuild)), 6)

    def test_vi(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Vi",self.currentBuild)), 6)

    def test_viego(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Viego", self.currentBuild)), 6)

    def test_viktor(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Viktor", self.currentBuild)), 6)

    def test_vladimir(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Vladimir", self.currentBuild)), 6)

    def test_volibear(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Volibear", self.currentBuild)), 6)

    def test_warwick(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Warwick", self.currentBuild)), 6)

    def test_wukong(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Xayah", self.currentBuild)), 6)

    def test_xerath(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Xerath", self.currentBuild)), 6)

    def test_xin_zhao(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "XinZhao",self.currentBuild)), 6)

    def test_yasuo(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Yasuo",self.currentBuild)), 6)

    def test_yone(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Yone", self.currentBuild)), 6)

    def test_yorick(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Yorick", self.currentBuild)), 6)

    def test_yuumi(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Yuumi",self.currentBuild)), 6)

    def test_zac(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Zac", self.currentBuild)), 6)

    def test_zed(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Zed", self.currentBuild)), 6)

    def test_ziggs(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Ziggs",self.currentBuild)), 6)

    def test_zilean(self):
         self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Zilean", self.currentBuild)), 6)

    def test_zoe(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Zoe",self.currentBuild)), 6)

    def test_zyra(self):
        self.assertEqual(len(bis_build.generate_build(self.items["data"], self.itemUsageDict, "Zyra", self.currentBuild)), 6)


if __name__ == "__main__":
    unittest.main()