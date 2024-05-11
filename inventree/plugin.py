# -*- coding: utf-8 -*-

import inventree.base


class InvenTreePlugin(inventree.base.MetadataMixin, inventree.base.InventreeObject):
    """Represents a PluginConfig instance on the InvenTree server."""

    URL = 'plugins'

    def setActive(self, active: bool):
        """Activate or deactivate this plugin."""

        url = f'plugins/{self.pk}/activate/'

        self._api.post(url, data={'active': active})