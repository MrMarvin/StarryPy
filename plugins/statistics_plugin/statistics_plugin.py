import logging
from base_plugin import BasePlugin
from core_plugins.player_manager import permissions, UserLevels

from sqlalchemy.orm import Session

from player_action import *

from player_manager.manager import PlayerManager
from packets import chat_send, warp_command

class Statistics(BasePlugin):
    """
    A plugin that collects various statistics and saves them for later processing.
    """
    name = "statistics_plugin"
    auto_activate = True
    
    def activate(self):
        super(Statistics, self).activate()
        logging.info("Statistics plugin activates...")
        self.engine = create_engine('sqlite:///plugins/statistics_plugin/statistics.db')
        self.session = Session(self.engine)
        StatisticsBase.metadata.create_all(self.engine)
        self.player_manager = PlayerManager(self.config)

    def deactivate(self):
        self.session.commit()
        self.session.close()
        self.active = False
        return True

    def after_client_connect(self, data):        
        self.session.add(PlayerAction(
            uuid=self.protocol.player.uuid,
            action_type=ActionTypes.CONNECTED,
            date_time=datetime.datetime.now()
            )        
        )
        self.session.commit()

    def after_client_disconnect(self, player):
        self.session.add(PlayerAction(
            uuid=player.uuid,
            action_type=ActionTypes.DISCONNECTED,
            date_time=datetime.datetime.now()
            )        
        )
        self.session.commit()

    def on_chat_sent(self, data):
        chat_line = chat_send.parse(data.data).message
        self.session.add(PlayerChatLine(
            uuid=self.protocol.player.uuid,
            date_time=datetime.datetime.now(),
            line=chat_line
            )        
        )
        self.session.commit()

    def after_warp_command(self, data):        
        warp = warp_command.parse(data.data)        
        self.session.add(PlayerWarps(
            uuid=self.protocol.player.uuid,
            date_time=datetime.datetime.now(),
            warp_type=warp.warp,
            warp_target=warp.player
            )
        )
        self.session.commit()

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