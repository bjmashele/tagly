import React from "react";
import { Flex, Text, Box, Link } from "rebass";

const Header = () => {
  return (
    <div>
      <Flex
        px={2}
        color="#41444b"
        // bg="#dbdbdb"
        height="7vh"
        alignItems="center"
      >
        <Text p={2} paddingRight="22vw" fontWeight="bold">
          Tagly
        </Text>

        <Text px={6} color="#41444b">
          Features
        </Text>
        <Text color="#41444b">Login</Text>
      </Flex>
    </div>
  );
};
export default function PublicPage() {
  return (
    <div>
      <Header></Header>

      <div className="welcome">Welcome</div>
    </div>
  );
}
