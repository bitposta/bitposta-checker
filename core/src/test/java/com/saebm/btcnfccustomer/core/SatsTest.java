package com.saebm.btcnfccustomer.core;

import org.junit.Test;
import static org.junit.Assert.*;

/** The card shows the same balance twice: exact sats, and the BTC a reader recognises. */
public class SatsTest {
    @Test public void btcKeepsEightDecimalsAndNeverRoundsAwayASmallBalance() {
        assertEquals("0.00000000", Sats.btc(0));
        assertEquals("0.00000001", Sats.btc(1));
        assertEquals("0.00000500", Sats.btc(500));
        assertEquals("1.00000000", Sats.btc(100_000_000L));
        assertEquals("21000000.00000000", Sats.btc(2_100_000_000_000_000L));
        assertEquals("-0.00000050", Sats.btc(-50));
    }
    @Test public void signedDeltaKeepsThePlusForAnIncrease() {
        assertEquals("+0.00000500", Sats.btcSigned(500));
        assertEquals("-0.00000050", Sats.btcSigned(-50));
        assertEquals("+0.00000000", Sats.btcSigned(0));
    }
}
