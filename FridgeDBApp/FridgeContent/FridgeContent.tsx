import React from "react";
import { FlatList, Text, View, Image } from "react-native";
import { shadow } from "react-native-paper";
import theme from "../Themes";

import { FridgeItem, FridgeItems } from "./data";

// style for the flatlist
const styles = {
    flatList: {
        flex: 1,
        paddingTop: 5,
        paddingBottom: 5,
        paddingLeft: 5,
        paddingRight: 5,
        backgroundColor: theme.colors.background,
    },
    row: {
        flex: 1,
        flexDirection: 'row',
        marginBottom: 5,
        marginTop: 5,
        marginLeft: 5,
        marginRight: 5,
        backgroundColor: 'white',
        borderRadius: theme.roundness,
        padding: 10,
        shadowColor: theme.colors.backdrop,
        shadowOffset: {
            width: 0,
            height: 1,
        },
        shadowOpacity: 0.20,
        shadowRadius: theme.roundness,

        elevation: 4,
    },
    image: {
        height: 60,
        width: 60,
    },
    itemName: {
        color: theme.colors.onAccent,
        fontSize: 18,
        fontWeight: 'bold',
    },
    text: {
        color: theme.colors.onAccent,
        fontSize: 14,
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
                <Text style={styles.itemName}>{item.name}</Text>
                <Text style={styles.text}>{item.category}</Text>
            </View>
            <View style={{ flex: 1, flexDirection: 'column', marginLeft: 10 }}>
                <Text style={styles.text}>Expiry: {item.expiry}</Text>
                <Text style={styles.text}>Quantity: {item.quantity}</Text>
            </View>
        </View >
    );
};

// FridgeContent component
const FridgeContent = () => {
    return (
        <View style={styles.flatList}>
            <FlatList
                data={FridgeItems}
                renderItem={({ item }) => <FridgeItemComponent item={item} />}
                style={styles.flatList}
            />
        </View>
    );
};

export default FridgeContent;
