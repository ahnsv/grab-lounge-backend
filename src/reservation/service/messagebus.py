from pybus.default.messagebus import DefaultMessageBus

from src.reservation.domain import commands
from src.reservation.service import handlers

messagebus = DefaultMessageBus()
messagebus.add_handler(commands.CreateReservation, handlers.create_reservation)
messagebus.add_handler(commands.ModifyReservation, handlers.modify_reservation)
messagebus.add_handler(commands.DeleteReservation, handlers.delete_reservation)
