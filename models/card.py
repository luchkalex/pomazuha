class Card:
    def __init__(
            self, 
            title: str, 
            image: str, 
            hp: int, 
            ad: int, 
            desc: str, 
            cost: int, 
            onShow, 
            onAttack
            ):
        
        self._title = title
        self._image = image
        self._hp = hp
        self._ad = ad
        self._desc = desc
        self._cost = cost
        self._onShow = onShow
        self._onAttack = onAttack

    def onShow(self):
        self._onShow()

    def onAttack(self):
        self._onAttack()


    
