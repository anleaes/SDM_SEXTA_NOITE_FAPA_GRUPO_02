class ClientSocialNetwork(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    socialNetwork = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Redes Social'
        verbose_name_plural = 'Itens de Rede Social'
        ordering =['id']

    def __str__(self):
        return self.socialNetwork.name 