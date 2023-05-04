from urllib.parse import  urlencode
from urllib.parse import quote
import sys
def test():
    s = "Dodot Sensitive Pañales Talla 2, 136 Unidades, 4-8kg"
    # s = "Envuelve a tu bebé en la máxima protección de la piel de Dodot. Dodot Sensitive es suave como una pluma, por eso proporciona una increíble sensación de suavidad para su piel. Además, gracias a su capa absorbente Cora-soft, ofrece la máxima absorción de caquita y pipí de Dodot, a la vez que cuida con total delicadeza de la piel de tu bebé. Capa absorbente Cora-soft que proporciona la máxima absorción de pipís y caquitas líquidas El indicador de humedad varía su color cuando tu bebé se ha hecho pipí El corte en la zona umbilical proporciona un ajuste suave y cómodo en la zona del ombligo Con canales de aire que mantienen la piel del bebé seca y aireada * Para evitar el riesgo de asfixia, mantenga esta bolsa y su asa alejada del alcance de los niños.  * Petrolatum, Stearyl Alcohol, Paraffinum Liquidum, Aloe Barbadensis Leaf Extract, CI 61565  ¿Quieres saber más sobre Dodot pañales componentes? Visíta en dodot.es  Política de devoluciones: el comprador será el responsable de pagar el coste del envío de devolución. | Disposable Diapers"
    s = "嗯，it is good, 呃，但我还是先那个嘛看看哈先"
    print(quote(s,encoding="utf-8"))
    s = "嗯，呃就是呃，我先试试吧，要是有啥问题，我就那个联系你"
    print(quote(s,encoding="utf-8"))
    s = "dodot|0-6m"
    print(quote(s,encoding="utf-8"))
    s = "Disposable Diapers"
    print(quote(s,encoding="utf-8"))

def quote_file():
    if len(sys.argv) < 3:
        print("usage: python do_urlencoder.py  smooth_test_rt.raw smooth_test_rt.txt" )
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    prefix="service=alitranx&version=tftransformer&domain=query&extinfo=ms202101v2&src_lang=en&trg_lang=zh&proc=32&xtm_proc=7&need_xrefine=false&need_xtm=true&need_cache=false&is_private=0&nbest=3&mtapp=query&need_trace=false&extra_params=scenario%3Dquery&xtm_refactor=true&appname=ovs-transformer&src=TMW&format=text&pvid=2887bb15-2093-45d2-846c-39a65eb3702b&query="
    #prefix="service=xrefine&src=dd&appname=speech_smooth_en&src_lang=en&model_type=nmt_smooth_en&model_version=1.0.0&model_domain=speech&nodetoken=true&query="
    with open(file_in) as fin, open(file_out, "w") as fout:
        for line in fin:
            fout.write(prefix + quote(line.strip(), encoding="utf-8")+"\n")

quote_file()


