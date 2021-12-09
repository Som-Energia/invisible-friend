!/usr/bin/env python3

subject = "PROVA: Amic Invisible Nadal 2020",
content="""\
AIXO ES UNA PROVA!!


Hola, {gifter.name}!

Gràcies per participar-hi :)

Ets l'amic/ga invisible de... **{gifted.name} {gifted.surname}**.

La seva adreça és:

{gifted.address}

Recorda enviar la postal abans del **24 de desembre**!

Una abraçada i feliços dies!
"""

import sys
from pathlib import Path
from yamlns import namespace as ns
import random
import emili

inputfile = Path(sys.argv[1]).read_text(encoding='utf8')
friends = [
    ns(
        name=name,
        surname=surname,
        email=email,
        address=address,
    )
    for name, surname, email, address in (
        line.split('\t')
        for line in inputfile.splitlines()
        if line.strip()
        and line.strip()[0] != '#'
    )
]
random.shuffle(friends)


for gifter, gifted in zip(friends, friends[1:]+friends[:1]):
    print(f"{gifter.name} {gifter.surname} <{gifter.email}> -> {gifted.name} {gifted.surname} <{gifted.email}>")
    continue
    emili.sendMail(
        sender  = "tomatic@somenergia.coop",
        to = [ gifter.email ],
        subject = subject,
        md = content.format(
            gifter=gifter,
            gifted=gifted,
        ),
        config = 'configdb.py',
    )

