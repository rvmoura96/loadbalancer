"""
Problema

Balanceamento de carga é muito importante em ambientes Cloud. Estamos sempre tentando minimizar os custos para que
possamos manter o número de servidores o menor possível. Em contrapartida a capacidade e performance aumenta quando
adicionamos mais servidores.

Em nosso ambiente de simulação, em cada tick (unidade básica de tempo da simulação), os usuários conectam aos
servidores disponíveis e executam uma tarefa. Cada tarefa leva um número de ticks para ser finalizada (o número de
ticks de uma tarefa é representado por ttask ), e após isso o usuário se desconecta automaticamente.
Os servidores são máquinas virtuais que se auto criam para acomodar novos usuários. Cada servidor custa R$ 1,00 por
tick e suporta no máximo umax usuários simultaneamente. Você deve finalizar servidores que não estão sendo mais usados.
O desafio é fazer um programa em Python que recebe usuários e os aloca nos servidores tentando manter o menor custo
possível.

Input
Um arquivo onde:
a primeira linha possui o valor de ttask ;
a segunda linha possui o valor de umax ;
as demais linhas contém o número de novos usuários para cada tick .


Constant value for tick cost COST_PER_TICK = 1.00
tick -> basic time unit
ttask -> ticks for a task conclusion
umax -> simultaneous user per server


"""


class Task:
    def __init__(self, ticks_to_conclusion):
        self.ticks_to_conclusion = ticks_to_conclusion

    def execute(self):
        self.ticks_to_conclusion -= 1

    @property
    def complete(self):
        return not self.ticks_to_conclusion