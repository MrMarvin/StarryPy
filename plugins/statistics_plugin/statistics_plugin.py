import logging
from base_plugin import SimpleCommandPlugin
from core_plugins.player_manager import permissions, UserLevels

from sqlalchemy.orm import Session

from player_action import *

class Statistics(SimpleCommandPlugin):
    """
    A plugin that collects various statistics and saves them for later processing.
    """
    name = "statistics_plugin"
    #commands = ["statistics"]
    auto_activate = True
    
    def activate(self):
        super(Statistics, self).activate()
        print("in activate")
        self.engine = create_engine('sqlite:///plugins/statistics_plugin/statistics.db')
        self.session = Session(self.engine)
        

    def deactivate(self):
        self.session.commit()
        self.session.close()
        self.active = False
        return True

    def after_chat_received(self, data):
        """
        Called after the chat_received packet is sent successfully.
        :return : None
        """

    def after_chat_sent(self, data):
        """
        Called after the chat_sent packet is sent successfully.
        :return : None
        """

    def after_client_connect(self, data):
        """
        Called after the client_connect packet is sent successfully.
        :return : None
        """

    def after_warp_command(self, data):
        """
        Called after the warp_command packet is sent successfully.
        :return : None
        """

    def after_context_update(self, data):
        """
        Called after the context_update packet is sent successfully.
        :return : None
        """

    def after_entity_interact(self, data):
        """
        Called after the entity_interact packet is sent successfully.
        :return : None
        """

    def after_open_container(self, data):
        """
        Called after the open_container packet is sent successfully.
        :return : None
        """

    def after_close_container(self, data):
        """
        Called after the close_container packet is sent successfully.
        :return : None
        """

    def after_swap_in_container(self, data):
        """
        Called after the swap_in_container packet is sent successfully.
        :return : None
        """

    def after_clear_container(self, data):
        """
        Called after the clear_container packet is sent successfully.
        :return : None
        """

    def after_world_update(self, data):
        """
        Called after the world_update packet is sent successfully.
        :return : None
        """

    def after_damage_notification(self, data):
        """
        Called after a damage notication packet is sent successfully.

        :return : None
        """