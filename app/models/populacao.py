from dataclasses import dataclass
from typing import Optional

@dataclass
class Populacao:
    """Model para representar um município brasileiro"""

    uf: str
    cod_uf: int
    cod_municipio: int
    nome_municipio: str
    capital_estado: str
    populacao: int
    id: Optional[int] = None

    def to_dict(self) -> dict:
        """Converte o objeto para dicionário"""
        return {
            "id": self.id,
            "uf": self.uf,
            "cod_uf": self.cod_uf,
            "cod_municipio": self.cod_municipio,
            "nome_municipio": self.nome_municipio,
            "capital_estado": self.capital_estado,
            "populacao": self.populacao,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Populacao":
        """Cria uma instância a partir de um dicionário"""
        return cls(
            id=data.get("id"),
            uf=data["uf"],
            cod_uf=data["cod_uf"],
            cod_municipio=data["cod_municipio"],
            nome_municipio=data["nome_municipio"],
            capital_estado=data["capital_estado"],
            populacao=data["populacao"],
        )

    def is_capital(self) -> bool:
        """Verifica se o município é uma capital"""
        return self.capital_estado.strip().lower() == "sim"

    def __str__(self) -> str:
        return f"{self.nome_municipio}/{self.uf}"

    def __repr__(self) -> str:
        return f"Municipio(id={self.id}, nome_municipio='{self.nome_municipio}', uf='{self.uf}')"
