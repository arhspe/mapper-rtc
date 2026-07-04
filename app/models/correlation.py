from pydantic import BaseModel, Field
from typing import List

class TaxClassification(BaseModel):
    cClassTrib: str = Field(..., example="000001", description="Código de Classificação Tributária")
    nome_cClassTrib: str = Field(..., example="Situações tributadas integralmente pelo IBS e CBS.", description="Nome da classificação tributária")

class OperationConfiguration(BaseModel):
    ps_onerosa: str = Field(..., example="S", description="Prestação de Serviço Onerosa (S/N)")
    adq_exterior: str = Field(..., example="N", description="Adquiriu no Exterior (S/N)")
    cIndOp: str = Field(..., validation_alias="IndOp", example="050101", description="Indicador de Operação")
    local_incidencia_ibs: str = Field(..., example="local da prestação", description="Regra de local de incidência do IBS")
    classificacoes_tributarias: List[TaxClassification] = Field(..., description="Classificações tributárias aplicáveis a esta operação")

class NbsService(BaseModel):
    codigo: str = Field(..., example="1.0105.70.00", description="Código da NBS")
    descricao: str = Field(..., example="Serviços de andaimes", description="Descrição da atividade na NBS")
    configuracoes_operacionais: List[OperationConfiguration] = Field(..., description="Lista de configurações operacionais vinculadas a esta NBS")

class CorrelationResponse(BaseModel):
    item_lc_116: str = Field(..., example="03.05", description="Código do item da Lei Complementar 116/2003")
    descricao_item: str = Field(..., example="Cessão De Andaimes, Palcos, Coberturas E Outras Estruturas De Uso Temporário.", description="Descrição oficial do item da LC 116")
    servicos_nbs: List[NbsService] = Field(..., description="Lista de serviços NBS vinculados hierarquicamente")