import { View, Text, StyleSheet } from 'react-native';
import React, { useCallback, useMemo, useRef } from 'react';
import BottomSheet from '@gorhom/bottom-sheet';

const CuBottomSheet = ({snapP}) => {

    const bottomSheetRef = useRef(null);   

    // variables
    const snapPoints = useMemo(() => snapP || ['25%', '50%'], []);

    const handleSheetChanges = useCallback((index) => {
        console.log('handleSheetChanges', index);
    }, []);
    
  return (
    <View style={styles.container}>
        <BottomSheet
            ref={bottomSheetRef}
            index={1}
            snapPoints={snapPoints}
            onChange={handleSheetChanges}
        >
            <View style={styles.contentContainer}>
            <Text>Awesome 🎉</Text>
            </View>
        </BottomSheet>
    </View>
  );
};


const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 24,
        backgroundColor: 'grey',
    },
    contentContainer: {
        flex: 1,
        alignItems: 'center',
    },
});

export default CuBottomSheet