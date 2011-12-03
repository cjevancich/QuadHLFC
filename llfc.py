import afprotowatcher
import logging
import struct

class State(object):
	def __init__(self, roll, pitch, yaw, x, y, z):
		self.roll = roll
		self.pitch = pitch
		self.yaw = yaw
		self.x = x
		self.y = y
		self.z = z

	def toBinaryString(self):
		return struct.pack('=ffffff', self.roll, self.pitch, self.yaw, self.x, self.y, self.z)

	def fromBinaryString(self, string):
		self.roll, self.pitch, self.yaw, self.x, self.y, self.z = struct.unpack('ffffff', string)

class Llfc(afprotowatcher.SerialAfprotoWatcher):
	def __init__(self, path='/dev/ttyUSB0', baudrate=115200):
		afprotowatcher.SerialAfprotoWatcher.__init__(self, path, baudrate)
		self.msg_handlers = {
			2: self.handle_debug_msg,
			3: self.handle_error_msg,
			4: self.handle_gyro_state,
			5: self.handle_accelero_state,
			6: self.handle_intertial_state }

	def handle_msg(self, msg):
		logging.debug('Got msg from LLFC')
		try:
			self.msg_handlers[ord(msg[0])](msg)
		except KeyError:
			pass

	def handle_debug_msg(self, msg):
		# trash the msg id byte
		msg = msg[1:]		
		
		# log debug message
		logging.debug('LLFC Debug: %s' % msg)

	def handle_error_msg(self, msg):
		# trash the msg id byte
		msg = msg[1:]

		# log error message
		logging.error('LLFC Error: %s' % msg)

	def handle_gyro_state(self, msg):
		logging.debug('LLFC Gyro State: Roll: %f\tPitch: %f\tYaw: %f' % struct.unpack('fff', msg[1:]))

	def handle_accelero_state(self, msg):
		logging.debug('LLFC Accelero State: X: %f\tY: %f\tZ: %f' % struct.unpack('fff', msg[1:]))

	def handle_intertial_state(self, msg):
		logging.debug('LLFC Inertial State: Roll: %f\tPitch: %f\tYaw: %f' % struct.unpack('fff', msg[:12]))

	def send_command(self, cmd_id, data):
		self.send_msg(chr(cmd_id) + data)

