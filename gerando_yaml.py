from troposphere import Ref, Template, ec2
from pprint import pprint

template = Template()

instancia =ec2.Instance(
    "MentoramaEscolaOnline",
    ImageId="ami-00534ec845573897f2",
    InstanceType="t2.micro",
)
template.add_resource(instancia)

template2 = Template()

instancia =ec2.Instance(
    "MonitoramentoDeServicos",
    ImageId="ami-00534ec828473897g9",
    InstanceType="t2.micro"
)
template2.add_resource(instancia)

template3 = Template()

instancia =ec2.Instance(
    "cursoPythonPRO",
    ImageId="ami-00534ec828834697h0",
    InstanceType="t2.micro"
)
template3.add_resource(instancia)

pprint(template.to_yaml())
pprint(template2.to_yaml())
pprint(template3.to_yaml())
