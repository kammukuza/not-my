# The MIT License (MIT)
# Copyright © 2024 Corsali, Inc. dba Vana

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import typing

import vana


class ValidationMessage(vana.Message):
    """
    This is the protocol for the validator to validator communication.
    It is a simple request-response protocol where the validator sends a request
    to other validators, and they respond back.

    ---- Elected validator ----
    Example usage:
      def validate( message: ValidationMessage ) -> ValidationMessage:
          message.output_is_valid = message.input_url is not None
          return message
      node_server = NodeServer().attach( validate ).serve(dlpuid=...).start()

    ---- validator ---
    Example usage:
      node_client = NodeClient()
      output_is_valid = node_client.query( ValidationMessage( input_url = "https://..." ) )
      assert output_is_valid == True
    """

    # Inputs filled by sending NodeClients.
    input_file_url: str

    # Outputs filled by receiving NodeServer.
    output_file_is_valid: typing.Optional[bool] = False

    output_file_score: typing.Optional[float] = 0.0

    def deserialize(self) -> dict:
        return {
            "output_file_is_valid": self.output_file_is_valid,
            "output_file_score": self.output_file_score,
        }
