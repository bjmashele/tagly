import React from "react";
import { Flex, Text, Box, Heading, Image } from "rebass";
import image from "../assets/tagly-icon.svg";
const Header = () => {
  return (
    <div>
      <Flex
        px={2}
        color="#41444b"
        // bg="#dbdbdb"
        height="7vh"
        alignItems="center"
        sx={{ display: "grid", width: "100%", justifyContent: "center" }}
      >
        <Text
          p={2}
          paddingRight="22vw"
          fontWeight="bold"
          fontFamily="Rockwell Extra Bold"
        >
          TAGLY
        </Text>

        <Text px={6} color="#41444b" className="text">
          Features
        </Text>
        <Text color="#41444b" className="text">
          Login
        </Text>
      </Flex>
    </div>
  );
};

const Main = () => {
  return (
    <Box
      sx={{
        paddingTop: "15vh",
        height: "75vh",
        display: "grid",
        // alignContent: "center",
        justifyContent: "center",
      }}
    >
      <Heading fontSize={[3, 4, 5]} color=" #f0a500">
        COLLECT, ORGANIZE, AND SHARE WEB LINKS WITH EASE.
      </Heading>
      <Image
        src={image}
        ml={7}
        mt={-4}
        sx={{
          width: ["100%", "50%"],
          display: "grid",
          justifyContent: "center",
        }}
      />
    </Box>
  );
};
export default function PublicPage() {
  return (
    <div>
      <Header></Header>
      <Main />
    </div>
  );
}
