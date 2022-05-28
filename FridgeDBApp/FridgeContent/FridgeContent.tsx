import { FlatList, Text, View, Image } from "react-native";
import theme from "../Themes";

import { FridgeItem, FridgeItems } from "./data";

// style for the flatlist
const styles = {
  flatList: {
    flex: 1,
    paddingTop: 5,
    paddingBottom: 5,
    paddingLeft: 10,
    paddingRight: 10,
    backgroundColor: 'white',
  },
  row: {
    flex: 1,
    flexDirection: 'row',
    marginBottom: 10,
    backgroundColor: 'white',
    borderRadius: 10,
    padding: 10,
    borderWidth: 3,
    borderColor: theme.fridgePrimary,
  },
  image: {
    height: 60,
    width: 60,
  },
};

// FridgeItem component for the FlatList
// align text next to image
const FridgeItemComponent = (props: { item: any; }) => {
  const { item } = props;
  return (
    <View style={styles.row}>
        <Image style={styles.image} source={item.image} />
        <View style={{ flex: 1, flexDirection: 'column', marginLeft: 10 }}>
            <Text style={{ fontSize: 20, fontWeight: 'bold' }}>{item.name}</Text>
            <Text style={{ fontSize: 15 }}>{item.category}</Text>
        </View>
        <View style={{ flex: 1, flexDirection: 'column', marginLeft: 10 }}>
            <Text style={{ fontSize: 15 }}>Expiry: {item.expiry}</Text>
            <Text style={{ fontSize: 15 }}>Quantity: {item.quantity}</Text>
        </View>
    </View>
  );
};

// FridgeContent component
const FridgeContent = () => {
  return (
    <View style={styles.flatList}>
      <FlatList
        data={FridgeItems}
        renderItem={({ item }) => <FridgeItemComponent item={item} />}
      />
    </View>
  );
};

export default FridgeContent;
