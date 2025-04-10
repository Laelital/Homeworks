from pydantic import BaseModel

class Breeds(BaseModel):
    affenpinscher: list[str | None]
    african: list[str | None]
    airedale: list[str | None]
    akita: list[str | None]
    appenzeller: list[str | None]
    australian: list[str | None]
    bakharwal: list[str | None]
    basenji: list[str | None]
    beagle: list[str | None]
    bluetick: list[str | None]
    borzoi: list[str | None]
    bouvier: list[str | None]
    boxer: list[str | None]
    brabancon: list[str | None]
    briard: list[str | None]
    buhund: list[str | None]
    bulldog: list[str | None]
    bullterrier: list[str | None]
    cattledog: list[str | None]
    cavapoo: list[str | None]
    chihuahua: list[str | None]
    chippiparai: list[str | None]
    chow: list[str | None]
    clumber: list[str | None]
    cockapoo: list[str | None]
    collie: list[str | None]
    coonhound: list[str | None]
    corgi: list[str | None]
    cotondetulear: list[str | None]
    dachshund: list[str | None]
    dalmatian: list[str | None]
    dane: list[str | None]
    danish: list[str | None]
    deerhound: list[str | None]
    dhole: list[str | None]
    dingo: list[str | None]
    doberman: list[str | None]
    elkhound: list[str | None]
    entlebucher: list[str | None]
    eskimo: list[str | None]
    finnish: list[str | None]
    frise: list[str | None]
    gaddi: list[str | None]
    germanshepherd: list[str | None]
    greyhound: list[str | None]
    groenendael: list[str | None]
    havanese: list[str | None]
    hound: list[str | None]
    husky: list[str | None]
    keeshond: list[str | None]
    kelpie: list[str | None]
    kombai: list[str | None]
    komondor: list[str | None]
    kuvasz: list[str | None]
    labradoodle: list[str | None]
    labrador: list[str | None]
    leonberg: list[str | None]
    lhasa: list[str | None]
    malamute: list[str | None]
    malinois: list[str | None]
    maltese: list[str | None]
    mastiff: list[str | None]
    mexicanhairless: list[str | None]
    mix: list[str | None]
    mountain: list[str | None]
    mudhol: list[str | None]
    newfoundland: list[str | None]
    otterhound: list[str | None]
    ovcharka: list[str | None]
    papillon: list[str | None]
    pariah: list[str | None]
    pekinese: list[str | None]
    pembroke: list[str | None]
    pinscher: list[str | None]
    pitbull: list[str | None]
    pointer: list[str | None]
    pomeranian: list[str | None]
    poodle: list[str | None]
    pug: list[str | None]
    puggle: list[str | None]
    pyrenees: list[str | None]
    rajapalayam: list[str | None]
    redbone: list[str | None]
    retriever: list[str | None]
    ridgeback: list[str | None]
    rottweiler: list[str | None]
    saluki: list[str | None]
    samoyed: list[str | None]
    schipperke: list[str | None]
    schnauzer: list[str | None]
    segugio: list[str | None]
    setter: list[str | None]
    sharpei: list[str | None]
    sheepdog: list[str | None]
    shiba: list[str | None]
    shihtzu: list[str | None]
    spaniel: list[str | None]
    spitz: list[str | None]
    springer: list[str | None]
    stbernard: list[str | None]
    terrier: list[str | None]
    tervuren: list[str | None]
    vizsla: list[str | None]
    waterdog: list[str | None]
    weimaraner: list[str | None]
    whippet: list[str | None]
    wolfhound: list[str | None]


class BreedsList(BaseModel):
    message: Breeds
    status: str


class BreedsImage(BaseModel):
    message: list[str] | str
    status: str
