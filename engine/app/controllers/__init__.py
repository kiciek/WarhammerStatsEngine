from .embed_controller import EmbedController
from .graph_controller import GraphController
from .inputs_controller import InputsController
from .link_controller import LinkController
from .static_controller import StaticController
from .url_controller import URLController

class CallbackController(object):
  def __init__(self, app, tab_count, weapon_count):
    self.app = app
    self.tab_count = tab_count
    self.weapon_count = weapon_count

    self.url_callback_controller = URLController(
      self.app,
      self.tab_count,
      self.weapon_count
    )

    self.graph_callback_controller = GraphController(
      self.app,
      self.tab_count,
      self.weapon_count
    )

    self.static_graph_callback_controller = StaticController(
      self.app,
      self.tab_count,
      self.weapon_count
    )

    self.embed_graph_callback_controller = EmbedController(
      self.app,
      self.tab_count,
      self.weapon_count
    )

    self.inputs_callback_controller = InputsController(
      self.app,
      self.tab_count,
      self.weapon_count
    )

    self.link_callback_controller = LinkController(
      self.app,
      self.tab_count,
      self.weapon_count
    )

  def setup_callbacks(self):
    self.url_callback_controller.setup_callbacks()
    self.graph_callback_controller.setup_callbacks()
    self.static_graph_callback_controller.setup_callbacks()
    self.inputs_callback_controller.setup_callbacks()
    self.link_callback_controller.setup_callbacks()




