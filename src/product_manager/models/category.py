from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    def get_descendants(self) -> list[Category]:
        descendants: list[Category] = []

        for child in self.children.all():
            descendants.append(child)
            descendants.extend(child.get_descendants())

        return descendants

    def __str__(self) -> str:
        return f"{self.name}, {self.parent}"
